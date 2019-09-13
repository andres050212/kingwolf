############## CÓDIGO MOVIMIENTO PARABÓLICO ###############
for i in $(seq 0 10);do
	echo | awk -v t=$i '{print cos(45)*t, sin(45)*t-((9.8*t*t)/2)}'
done
