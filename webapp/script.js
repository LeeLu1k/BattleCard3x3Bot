const tg = window.Telegram.WebApp;
tg.expand();

const user = tg.initDataUnsafe?.user;

if (user) {
    const name = user.username 
        ? `@${user.username}` 
        : `${user.first_name || ''} ${user.last_name || ''}`.trim();
    document.getElementById("userName").textContent = name || "Игрок";
} else {
    document.getElementById("userName").textContent = "Гость";
}

document.getElementById("startGame").addEventListener("click", () => {
    tg.sendData(JSON.stringify({ action: "start_game" }));
    alert("🎮 Игра скоро начнётся!");
});
