PS1='\[\e[0;32m\]\u\[\e[0;37m\]@\h:\w \[\e[0;92m\]♧\[\e[97m\]  '
complete -d cd
alias apt-stuff='sudo apt-get update; sudo apt-get upgrade; sudo apt-get autoremove; sudo apt-get autoclean'
alias clock='while true; do date; echo -ne "\033[1F"; sleep 1; done'
alias del='rm -frv'
alias hi='history'
alias list='ls -ahls --color=auto'
alias please='sudo'
alias rv='find . -name "*~" -exec rm -v '{}' \; && find . -name "#*#" -exec rm -v '{}' \;'
alias tree='tree -C'
say () { pico2wave -w="tmp.wav" "$@" &> /dev/null; aplay "tmp.wav" &> /dev/null; rm "tmp.wav" &> /dev/null; }
exists () { printf "The \"%s\" command does " $1; if ! command -v $1 &> /dev/null; then printf "not "; fi; printf "exist.\n"; }
up () { for ((i=1; i <= $1; i++)) do cd ..; done; }
