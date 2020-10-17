from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

import sys
if sys.platform.startswith("win"):
    import _locale
    # pylint: disable=protected-access
    _locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(args=['english', 'all', 'hello'])]

    def check(self, reply, attach):
        reply = reply.lower().strip()
        if not ('arabic translation' in reply
                and 'arabic example' in reply
                and 'russian translation' in reply
                and 'russian example' in reply
                and 'german translation' in reply
                and 'spanish translation' in reply):
            return CheckResult.wrong("Try to print translations and examples of all languages you can.")

        if not ('bonjour' in reply and 'hallo' in reply and 'hola' in reply):
            return CheckResult.wrong("Looks like you did not print translations for some of the languages for which you printed the titles\n"
                                     "(titles such as \"... translations\", where ... is the name of the language)")

        if 'french translations' not in reply and 'french examples' not in reply:
            return CheckResult.wrong("Maybe there is a mistake in command line args or in output.\n\
                 if args==['english', 'french', 'hello'], your output should contain \
                 'french translations', 'french examples' and so on")

        russian_examples_index = reply.index('russian example')
        try:
            end_of_re_index = reply[russian_examples_index:].index('translation') + russian_examples_index
            ru_examples_slice = reply[russian_examples_index:end_of_re_index]
            end_of_re_index = ru_examples_slice.rindex('\n') + russian_examples_index
        except ValueError:
            end_of_re_index = None

        russian_examples_slice = reply[russian_examples_index:end_of_re_index].strip().split('\n')

        if len(russian_examples_slice) < 3:
            return CheckResult.wrong("Looks like you did not print examples for some of the languages for which you printed the titles\n"
                                     "(titles such as \"... translations\", where ... is the name of the language)\n"
                                     "Remember that the title, the example in the original language and its translation should be printed on separate lines.\n"
                                     "For example:\n"
                                     "\"French examples:\n"
                                     "Well, hello, freedom fighters\n"
                                     "Et bien, bonjour combattants de la libert?.\"")

        return CheckResult.correct()




if __name__ == '__main__':
    TranslatorTest('translator.translator').run_tests()
