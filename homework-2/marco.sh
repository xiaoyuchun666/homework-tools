#!/bin/bash
marco_dir=""
marco(){
	marco_dir=$(pwd)
	echo "current dir saced:$marco_dir"
}

polo(){
	if [ -n "$marco_dir" ];then
		cd "$marco_dir" || echo "Failed to change dir to $marco_dir"
		echo "Changed dir to : $marco_dir"
	else
		echo "No dir saved."
	fi
}
