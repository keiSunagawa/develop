set -x PATH /home/kerfume/.nix-profile/bin $PATH

# tmux alias
function tn
  tmux new -s $argv[1]
end

function ta
  tmux new a -t $argv[1]
end

function tl
  tmux tmux ls
end
