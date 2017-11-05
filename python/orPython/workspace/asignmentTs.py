import gachon_autograder_client as g_auto
import sys


THE_TEAMLABIO_ID = "teamlab.test"
PASSWOD = "test1234"
ASSIGNMENT_FILE_NAME = sys.argv[1]

g_auto.get_assignment(THE_TEAMLABIO_ID, PASSWOD, ASSIGNMENT_FILE_NAME)
#g_auto.submit_assignment(THE_TEAMLABIO_ID, PASSWOD, ASSIGNMENT_FILE_NAME)
