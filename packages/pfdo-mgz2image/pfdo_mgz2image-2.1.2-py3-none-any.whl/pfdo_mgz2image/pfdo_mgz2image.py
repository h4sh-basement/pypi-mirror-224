# Turn off all logging for modules in this libary.
import logging
logging.disable(logging.CRITICAL)

# System imports
import      os
import      json
import      pathlib
from        argparse            import  Namespace

# Project specific imports
import      pfmisc
from        pfmisc._colors      import  Colors
from        pfmisc              import  other
from        pfmisc              import  error

from        mgz2imgslices       import  mgz2imgslices
from        pfdo                import  pfdo

import      pudb
import      pftree

class pfdo_mgz2image(pfdo.pfdo):
    """

    A class for navigating down a dir tree and providing
    hooks for some (subclass) analysis

    """

    _dictErr = {
        'outputDirFail'   : {
            'action'        : 'trying to check on the output directory, ',
            'error'         : 'directory not specified. This is a *required* input.',
            'exitCode'      : 1},
        'outputFileExists'   : {
            'action'        : 'attempting to write an output file, ',
            'error'         : 'it seems a file already exists. Please run with --overwrite to force overwrite.',
            'exitCode'      : 2}
        }


    def declare_selfvars(self):
        """
        A block to declare self variables
        """

        #
        # Object desc block
        #
        self.str_desc                   = ''
        self.__name__                   = "pfdo_mgz2image"

    def __init__(self, *args, **kwargs):
        """
        Constructor for pfdo_mgz2image.

        This basically just calls the parent constructor and
        adds some child-specific data.
        """

        super().__init__(*args, **kwargs)

        pfdo_mgz2image.declare_selfvars(self)

    def inputReadCallback(self, *args, **kwargs):
        """
        This method does not actually read in any files, but
        exists to preserve the list of files associated with a
        given input directory.

        By preserving and returning this file list, the next
        callback function in this pipeline is able to receive an
        input path and a list of files in that path.
        """
        str_path        : str       = ''
        l_fileProbed    : list      = []
        b_status        : bool      = True
        filesProbed     : int       = 0
        str_outputWorkingDir: str       = ""

        if len(args):
            at_data         = args[0]
            str_path        = at_data[0]
            l_fileProbed    = at_data[1]

        # Need to create the output dir appropriately here!
        str_outputWorkingDir    = str_path.replace(
                                        self.args['inputDir'],
                                        self.args['outputDir']
        )
        self.dp.qprint("mkdir %s" % str_outputWorkingDir,
                        level = 3)
        other.mkdir(str_outputWorkingDir)

        if not len(l_fileProbed): b_status = False

        return {
            'status':           b_status,
            'l_fileProbed':     l_fileProbed,
            'str_path':         str_path,
            'filesProbed':      filesProbed
        }

    def inputAnalyzeCallback(self, *args, **kwargs):
        """
        Callback stub for doing actual work. Since the `mgz2imgslices`
        is a mostly stand-apart module, the inputRead and outputWrite
        callbacks are not applicable here, since calling the
        `mgz2imgslices` module appropriately reads an input and saves
        an output.
        """

        def l_fileToAnalyze_determine(l_fileProbed):
            """
            Return the list of files to process, based on l_fileProbed
            and self.args['analyzeFileIndex']
            """

            def middleIndex_find(l_lst):
                """
                Return the middle index in a list.
                If list has no length, return None.
                """
                middleIndex     = None
                if len(l_lst):
                    if len(l_lst) == 1:
                        middleIndex = 0
                    else:
                        middleIndex = round(len(l_lst)/2+0.01)
                return middleIndex

            def nIndex_find(l_lst, str_index):
                """
                For a string index, say "2", return the index at l_lst[2].
                If index is out of bounds return None.
                """
                index:  int = 0
                try:
                    index   = int(str_index)
                    if len(l_lst):
                        if index >= -1 and index < len(l_lst):
                            return index
                except:
                    pass
                return None

            l_fileToAnalyze:    list    = []
            if len(l_fileProbed):
                if self.args['analyzeFileIndex'] == 'f': l_fileToAnalyze.append(l_fileProbed[0])
                if self.args['analyzeFileIndex'] == 'l': l_fileToAnalyze.append(l_fileProbed[-1])
                if self.args['analyzeFileIndex'] == 'm':
                    if middleIndex_find(l_fileProbed) >= 0:
                        self.dp.qprint(l_fileProbed, level = 5)
                        l_fileToAnalyze.append(l_fileProbed[middleIndex_find(l_fileProbed)])
                nIndex  = nIndex_find(l_fileProbed, self.args['analyzeFileIndex'])
                if nIndex:
                    if nIndex == -1:
                        l_fileToAnalyze = l_fileProbed
                    else:
                        l_fileToAnalyze.append(nIndex)
            return l_fileToAnalyze

        b_status            : bool  = False
        l_fileProbed        : list  = []
        d_inputReadCallback : dict  = {}
        d_convert           : dict  = {}


        for k, v in kwargs.items():
            if k == 'path':         str_path    = v

        if len(args):
            at_data             = args[0]
            str_path            = at_data[0]
            d_inputReadCallback = at_data[1]
            l_fileProbed        = d_inputReadCallback['l_fileProbed']

        # pudb.set_trace()
        mgz2image_args                  = self.args.copy()
        # print(at_data)

        for str_file in l_fileToAnalyze_determine(l_fileProbed):
            mgz2image_args['inputDir']      = str_path
            mgz2image_args['inputFile']     = str_file
            mgz2image_args['outputDir']     = str_path.replace(
                                                self.args['inputDir'],
                                                self.args['outputDir']
                                            )

            mgz2image_args['outputDir'] = os.path.join(mgz2image_args['outputDir'], str_file)
            other.mkdir(mgz2image_args['outputDir'])

            mgz2image_args['saveImages']    = self.args['saveImages']
            mgz2image_args['skipAllLabels'] = self.args['skipAllLabels']

            mgz2image_ns    = Namespace(**mgz2image_args)

            # Note that the imgConverter has an implicit assumption on an existing
            # /usr/src/FreeSurferColorLUT.txt!
            try:
                imgConverter    = mgz2imgslices.object_factoryCreate(mgz2image_ns).C_convert
            except Exception as e:
                self.dp.qprint(e, comms = 'error', level = 0)

            # At time of dev, the `imgConverter.run()` does not return anything.
            imgConverter.run()

        return {
            'status':           b_status,
            'str_path':         str_path,
            'l_fileProbed':     l_fileProbed,
            'd_convert':        d_convert
        }

    def filelist_prune(self, at_data, *args, **kwargs) -> dict:
        """
        Given a list of files, possibly prune list by
        interal self.args['filter'].
        """

        # pudb.set_trace()

        b_status    : bool      = True
        l_file      : list      = []
        str_path    : str       = at_data[0]
        al_file     : list      = at_data[1]

        if len(self.args['filter']):
            file_list = self.args['filter'].split(',')

        for file in file_list:
            for a_file in al_file:
                if file in a_file:
                    l_file.append(a_file)

        if len(l_file):
            l_file.sort()
            b_status    = True
        else:
            self.dp.qprint( "No valid files to analyze found in path %s!" %
                            str_path, comms = 'warn', level = 5)
            l_file      = None
            b_status    = False
        return {
            'status':   b_status,
            'l_file':   l_file
        }

    def mgz2image(self) -> dict:
        """
        The main entry point for connecting methods of this class
        to the appropriate callbacks of the `pftree.tree_process()`.
        Note that the return json of each callback is available to
        the next callback in the queue as the second tuple value in
        the first argument passed to the callback.
        """
        d_mgz2image     : dict    = {}

        other.mkdir(self.args['outputDir'])
        d_mgz2image     = self.pf_tree.tree_process(
                            inputReadCallback       = self.inputReadCallback,
                            analysisCallback        = self.inputAnalyzeCallback,
                            outputWriteCallback     = None,
                            persistAnalysisResults  = False
        )
        return d_mgz2image

    def run(self, *args, **kwargs) -> dict:
        """
        This base run method should be called by any descendent classes
        since this contains the calls to the first `pftree` prove as well
        as any (overloaded) file filtering.
        """

        # pudb.set_trace()
        # print("***********")
        b_status        : bool  = False
        b_timerStart    : bool  = False
        d_pfdo          : dict  = {}
        d_mgz2image     : dict  = {}

        self.dp.qprint(
                "Starting pfdo_mgz2image run... (please be patient while running)",
                level = 1
        )

        for k, v in kwargs.items():
            if k == 'timerStart':   b_timerStart    = bool(v)

        if b_timerStart:    other.tic()

        # pudb.set_trace()
        d_pfdo          = super().run(
                            JSONprint   = False,
                            timerStart  = False
        )

        if d_pfdo['status']:
            d_mgz2image     = self.mgz2image()

        d_ret = {
            'status':           b_status,
            'd_pfdo':           d_pfdo,
            'd_mgz2image':      d_mgz2image,
            'runTime':          other.toc()
        }

        if self.args['json']:
            self.ret_dump(d_ret, **kwargs)
        else:
            self.dp.qprint('Returning from pfdo_mgz2image class run...', level = 1)

        return d_ret