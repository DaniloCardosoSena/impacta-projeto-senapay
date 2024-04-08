document.addEventListener('DOMContentLoaded', function() {
    const deleteButton = document.getElementById('delete-btn');
    if (deleteButton) {
        deleteButton.addEventListener('click', function(event) {
            const confirmed = confirm('Tem certeza que deseja excluir sua conta?');
            if (!confirmed) {
                event.preventDefault(); // Cancela o comportamento padrão do botão se a exclusão não for confirmada
            }
        });
    }
});