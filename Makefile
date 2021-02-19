#
# Development by Carl J. Nobile
#

PREFIX		= $(shell pwd)
BASE_DIR        = $(shell echo $${PWD\#\#*/})
DOCS_DIR	= $(PREFIX)/docs
TODAY		= $(shell date +"%Y-%m-%d_%H%M")
RM_REGEX	= '(^.*.pyc$$)|(^.*.wsgic$$)|(^.*~$$)|(.*\#$$)|(^.*,cover$$)'
RM_CMD		= find $(PREFIX) -regextype posix-egrep -regex $(RM_REGEX) \
                  -exec rm {} \;
PIP_ARGS	=

#----------------------------------------------------------------------
all	: tar

#----------------------------------------------------------------------
tar	: clean
	@(cd ..; tar -czvf $(PACKAGE_DIR).tar.gz --exclude=".git" \
          --exclude="dist/*" $(PACKAGE_DIR))

docs: clean
	@(cd $(DOCS_DIR); make)

.PHONY	: install-dev
install-dev:
	pip install $(PIP_ARGS) -r requirements.txt

.PHONY	: coverage
coverage: clean
	@rm -rf $(DOCS_DIR)/htmlcov
	@nosetests --with-coverage --cover-erase --nocapture \
                   --cover-package=mimeparser --cover-package=xml2dict
	@coverage html

#----------------------------------------------------------------------

clean	:
	$(shell $(RM_CMD))

clobber	: clean
	@rm -rf *.egg-info
	@rm -rf dist
	@rm -rf $(DOCS_DIR)/htmlcov
