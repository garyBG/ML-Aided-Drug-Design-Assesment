##PREREQUISITE INSTALLS NEEDED TO USE SELENIUM FOR MAC

# INSTALL HOMEBREW
# HOMEBREW'S WEBSITE: https://brew.sh/
#HOMEBREW INSTALL CODE FOR MAC:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

#INSTALL GIT FROM HOMEBREW
#HOMEBREW'S WEBSITE FOR GIT INSTALLATION: https://formulae.brew.sh/formula/git#default
#GIT CODE FOR MAC:
brew install git

# INSTALL CHROMEDRIVER FOR SELENIUM
# CHROMEDRIVER INSTALLATION WEBSITE: https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver
brew install --cask chromedriver



#INSTALL SELENIUM:
pip install selenium
