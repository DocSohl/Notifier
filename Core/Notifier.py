import sys
import traceback
import logging

class Notifier:
    def __init__(self):
        logging.basicConfig(filename="Logs/notifier.log")
        self._logger = logging.getLogger("notifier")
    
    def run(self):
        while 1:
            try:
                pass
            except (KeyboardInterrupt, SystemExit):
                raise
            except Exception, e:
                print traceback.format_exc()
                self._logger.warn("Error in main loop", exc_info=True)
            finally:
                pass
                



if __name__=="__main__":
    app = Notifier()
    app.run()
    sys.exit()