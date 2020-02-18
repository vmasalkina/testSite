function getGraphData (data, step) {
  //Начальное время
  var time0 = Object.keys(data)[0];
  if (time0 === undefined) {
    return false
  };
  var fTime = time0.split('.')[0].slice(0,-2)+'00';
  var iTime = parseInt(fTime);
  const ms = (step == '5') ? 300 : 1800;
  for (let i = 0; i < ms; i=i+100) {
    if ((iTime+i)%ms == 0) {
      time0 = iTime+i-ms;
  }};
  //Координаты х-начальное время для каждых 5/30 мин; у-значение
  const x0 = new Date((time0)*1000);
  var X = [];
  var Ymin = [];
  var Yave = [];
  var Ymax = [];
  //Значения за один 5/30минутный интервал
  var y = [];
  for (let time in data) {
    if (time >= time0) {
      if (y.length != 0) {
        Ymin.push(Math.min(...y));
        Ymax.push(Math.max(...y));
        Yave.push(y.reduce((a, b) => (a + b)) / y.length);
      };
      y = [];
      while (time >= time0) {
	time0 = time0 + ms;
      };
      X.push(new Date((time0-ms)*1000));
    };
    y.push(data[time]);
  };
  Ymin.push(Math.min(...y));
  Ymax.push(Math.max(...y));
  Yave.push(y.reduce((a, b) => (a + b)) / y.length);
  return [X, Ymin, Ymax, Yave, x0]
}



