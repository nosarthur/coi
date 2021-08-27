
_coi_completions()
{

  local cur commands repos cmd

  cur=${COMP_WORDS[COMP_CWORD]}
  cmd=${COMP_WORDS[1]}
  cmd2=${COMP_WORDS[2]}

  if [ $COMP_CWORD -eq 1 ]; then
    commands="run template"
    COMPREPLY=($(compgen -W "${commands}" ${cur}))
  #if [ $COMP_CWORD -eq 2 ]; then
  elif [ $COMP_CWORD -gt 1 ]; then
    case $cmd in
      run)
        case $cmd2 in
          -t)
            ts=`coi template ls`
            COMPREPLY=($(compgen -W "$ts") $cur)
            ;;
          *)
            COMPREPLY=($(compgen -d ${cur}))
            ;;
        esac
        ;;
      template)
        COMPREPLY=($(compgen -W "ll set ls rm add cp" ${cur}))
        ;;
      ll | ls | rm)
        ts=`coi template ls`
        COMPREPLY=($(compgen -W $ts))
        return
        ;;
    esac
  fi
}

complete -F _coi_completions coi

