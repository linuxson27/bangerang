def translate_error(error):
    if "Cmd('git') failed due to: exit code(128)" in str(error):
        return(['Git Comms Error',
            'Unable to access the online repository. Please retry in a short while, or contact your system administrator'])
    else:
        return ['General Error', str(error)]