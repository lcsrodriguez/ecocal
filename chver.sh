if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
    exit 1
fi
OLD_VER=$1
NEW_VER=$2
echo ${OLD_VER} "->" ${NEW_VER}
echo "----------- Files -----------"
grep -rl --exclude-dir=.git --exclude-dir=venv -I $1 . # Excluding binaries
grep -rl --exclude-dir=.git --exclude-dir=venv -I $1 . | xargs sed -i "" -e "s/${OLD_VER}/${NEW_VER}/g"