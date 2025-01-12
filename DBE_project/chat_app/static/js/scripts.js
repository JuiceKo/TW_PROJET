// Gestion des modales
const modalCreateGroup = document.getElementById('modal-create-group');
const modalAddFriend = document.getElementById('modal-add-friend');

// Boutons pour ouvrir les modales
document.getElementById('create-group').addEventListener('click', () => {
    modalCreateGroup.style.display = 'block';
});

document.getElementById('add-friend').addEventListener('click', () => {
    modalAddFriend.style.display = 'block';
});

// Boutons pour fermer les modales
document.getElementById('close-create-group').addEventListener('click', () => {
    closeModal(modalCreateGroup);
});

document.getElementById('close-add-friend').addEventListener('click', () => {
    closeModal(modalAddFriend);
});

// Fonction pour fermer une modale
function closeModal(modal) {
    modal.style.display = 'none';
}

// Fonction pour valider et enregistrer un groupe
document.getElementById('save-group').addEventListener('click', () => {
    const groupName = document.getElementById('group-name').value.trim();
    if (groupName) {
        alert(`Groupe créé : ${groupName}`); 
        closeModal(modalCreateGroup);
        resetInput('group-name'); 
    } else {
        alert('Veuillez entrer un nom de groupe.');
    }
});

// Fonction pour valider et enregistrer un ami
document.getElementById('save-friend').addEventListener('click', () => {
    const friendName = document.getElementById('friend-name').value.trim();
    if (friendName) {
        alert(`Ami ajouté : ${friendName}`); 
        closeModal(modalAddFriend);
        resetInput('friend-name'); // Réinitialiser le champ
    } else {
        alert('Veuillez entrer le nom d’un ami.');
    }
});

// Fermer la modale en cliquant en dehors de son contenu
window.addEventListener('click', (event) => {
    if (event.target === modalCreateGroup) {
        closeModal(modalCreateGroup);
    }
    if (event.target === modalAddFriend) {
        closeModal(modalAddFriend);
    }
});

// Fonction pour réinitialiser un champ d'entrée
function resetInput(inputId) {
    document.getElementById(inputId).value = '';
}

// Filtrage des groupes en fonction de la recherche
function filterGroups() {
    const input = document.getElementById('search-groups');
    const filter = input.value.toLowerCase();
    const ul = document.getElementById('group-list');
    const li = ul.getElementsByTagName('li');

    for (let i = 0; i < li.length; i++) {
        const a = li[i].getElementsByTagName('a')[0];
        if (a.innerHTML.toLowerCase().includes(filter)) {
            li[i].style.display = '';
        } else {
            li[i].style.display = 'none';
        }
    }
}






















fetch('/api/create-group/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({ name: groupName }),
})
.then(response => response.json())
.then(data => {
    if (data.success) {
        alert(`Groupe créé : ${groupName}`);
        closeModal(modalCreateGroup);
        resetInput('group-name');
    } else {
        alert('Une erreur s\'est produite.');
    }
})
.catch(error => console.error('Erreur:', error));
