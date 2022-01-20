from app import app
import uvicorn

from optparse import OptionParser

if __name__ == '__main__':

    #To do any actions/checks before server starts
    
    parser = OptionParser()
    parser.add_option('-d', '--debug', dest='debug', help="To run app in debug mode", action='store_true', default=False)
    parser.add_option('-r', '--reload', dest='reload', help="Hot-reloading", action='store_true', default=False)

    (options, args) = parser.parse_args()

    uvicorn.run(app, debug=options.debug, reload=options.reload, host="127.0.0.1", port="8000")