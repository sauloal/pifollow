set -xeu
#CLOUD9
URL_BASE=http://pifollowjs-sauloal.c9.io
APV=1
EPN=api/v${APV}
RNG='54628'
RNG_URL=''
PI_NAME=piname

if [[ ! -z "${RNG}" ]]; then
	RNG_URL="/${RNG}"
fi

URL=${URL_BASE}${RNG_URL}

API=${URL}/${EPN}

