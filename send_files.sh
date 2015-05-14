RND=$1
PINAME=$2
FN=$3

if [[ -z "$RND" ]]; then
        echo NO RANDON NUMBER PASSED
fi
if [[ -z "$PINAME" ]]; then
        echo NO PINAME PASSED
fi
if [[ -z "$FN" ]]; then
        echo NO FILE NAME GIVEN
fi


FN=`readlink -f $FN`

curl -X POST --form foto=@"$FN" http://pi-sauloal.c9.io/$RND/add/$PINAME
