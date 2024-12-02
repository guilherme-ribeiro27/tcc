#--------------INSTALAÇÃO DO PYENV -----------------------
wget -qO- https://pyenv.run | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc

echo 'command -v pyenv > /dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc

echo 'eval "$(pyenv init -)"' >> ~/zshrc

exec "$SHELL"

#--------------INSTALAÇÃO DO PYENV -----------------------

