<div id="pomodoro">
  <div id="vreme">25:00</div>
  <div id="status">Fokus</div>
  <div id="dugmici">
    <button onclick="startuj()">▶ Start</button>
    <button onclick="pauziraj()">⏸ Pauza</button>
    <button onclick="resetuj()">↺ Reset</button>
  </div>
</div>

<script>
var trajanje = 25 * 60;
var preostalo = trajanje;
var interval = null;
var jePauza = false;

function azuriraj() {
  var min = Math.floor(preostalo / 60);
  var sek = preostalo % 60;
  document.getElementById('vreme').textContent =
    (min < 10 ? '0' : '') + min + ':' + (sek < 10 ? '0' : '') + sek;
}

function startuj() {
  if (interval) return;
  interval = setInterval(function() {
    if (preostalo <= 0) {
      clearInterval(interval);
      interval = null;
      document.getElementById('status').textContent = jePauza ? 'Fokus!' : 'Pauza!';
      jePauza = !jePauza;
      preostalo = jePauza ? 5 * 60 : 25 * 60;
      new Audio('https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3').play();
      return;
    }
    preostalo--;
    azuriraj();
  }, 1000);
}

function pauziraj() {
  clearInterval(interval);
  interval = null;
}

function resetuj() {
  clearInterval(interval);
  interval = null;
  jePauza = false;
  preostalo = 25 * 60;
  document.getElementById('status').textContent = 'Fokus';
  azuriraj();
}
</script>

<style>
#pomodoro {
  text-align: center;
  padding: 20px;
  margin: 20px 0;
}
#vreme {
  font-size: 4em;
  font-weight: bold;
  font-family: monospace;
}
#status {
  font-size: 1.2em;
  margin: 10px 0;
  opacity: 0.7;
}
#dugmici button {
  margin: 5px;
  padding: 10px 20px;
  font-size: 1em;
  cursor: pointer;
  border: none;
  border-radius: 8px;
  background: var(--md-primary-fg-color);
  color: white;
}
</style>