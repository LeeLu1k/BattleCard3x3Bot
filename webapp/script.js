const tg = window.Telegram.WebApp;
tg.expand();

const btnCards = document.getElementById("btnCards");
const btnPack = document.getElementById("btnPack");
const btnFight = document.getElementById("btnFight");
const collection = document.getElementById("collection");
const pack = document.getElementById("pack");
const packResult = document.getElementById("packResult");

function hideAll() {
  collection.classList.add("hidden");
  pack.classList.add("hidden");
}

btnCards.onclick = () => {
  hideAll();
  collection.classList.remove("hidden");
};

btnPack.onclick = () => {
  hideAll();
  pack.classList.remove("hidden");
  packResult.innerHTML = "🎲 Бросаем кости...";

  setTimeout(() => {
    const rarities = ["Common", "Rare", "Epic", "Legendary"];
    const rarity = rarities[Math.floor(Math.random() * rarities.length)];
    packResult.innerHTML = `<div class="card ${rarity.toLowerCase()}">✨ ${rarity} Card!</div>`;
    tg.MainButton.text = "Добавить карту";
    tg.MainButton.show();
  }, 1500);
};

btnFight.onclick = () => {
  tg.sendData("fight_start");
  alert("⚔️ Ты вступаешь в бой!");
};
