# Dobrodošli na Laganica Wiki

<div id="pomodoro">
  <div id="vreme">25:00</div>
  <div id="status">Fokus</div>

  <div id="custom-vreme">
    <label>Fokus (min): <input type="number" id="custom-fokus" min="1" max="120" value="25" style="width:50px; padding:4px; border-radius:6px; border:1px solid #ccc; text-align:center;"></label>
    <label>Kratka pauza (min): <input type="number" id="custom-kratka" min="1" max="60" value="5" style="width:50px; padding:4px; border-radius:6px; border:1px solid #ccc; text-align:center;"></label>
    <label>Duga pauza (min): <input type="number" id="custom-duga" min="1" max="60" value="15" style="width:50px; padding:4px; border-radius:6px; border:1px solid #ccc; text-align:center;"></label>
  </div>

  <div id="rezimi">
    <button onclick="postaviRezim(getFokus(), 'Fokus')">🎯 Fokus</button>
    <button onclick="postaviRezim(getKratka(), 'Kratka pauza')">☕ Kratka pauza</button>
    <button onclick="postaviRezim(getDuga(), 'Duga pauza')">🛋️ Duga pauza</button>
  </div>

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

function getFokus() { return parseInt(document.getElementById('custom-fokus').value) || 25; }
function getKratka() { return parseInt(document.getElementById('custom-kratka').value) || 5; }
function getDuga() { return parseInt(document.getElementById('custom-duga').value) || 15; }

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
  preostalo = trajanje;
  azuriraj();
}

function postaviRezim(minuta, naziv) {
  clearInterval(interval);
  interval = null;
  trajanje = minuta * 60;
  preostalo = trajanje;
  document.getElementById('status').textContent = naziv;
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
#custom-vreme {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
  margin: 12px 0;
  font-size: 0.9em;
}
#rezimi button, #dugmici button {
  margin: 5px;
  padding: 8px 16px;
  font-size: 0.95em;
  cursor: pointer;
  border: none;
  border-radius: 8px;
  background: var(--md-primary-fg-color);
  color: white;
}
#rezimi { margin: 8px 0; }
#dugmici { margin-top: 10px; }
</style>