document.addEventListener('DOMContentLoaded', () => {
    const emojiPickerBtn = document.getElementById('emoji-picker-btn');
    const emojiPicker = document.getElementById('emoji-picker');
    const inputField = document.getElementById('message-input');

    if (!emojiPickerBtn || !emojiPicker) {
        console.error('Bouton ou sélecteur d\'emojis introuvable.');
        return;
    }

    // Affiche ou masque le sélecteur d'emojis
    emojiPickerBtn.addEventListener('click', () => {
        emojiPicker.classList.toggle('hidden');
    });

    // Ajouter l'emoji sélectionné au champ d'entrée
    document.querySelectorAll('.emoji-btn').forEach(button => {
        button.addEventListener('click', function () {
            const emoji = this.textContent;
            inputField.value += emoji;
            emojiPicker.classList.add('hidden');
        });
    });
});
