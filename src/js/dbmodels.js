document.addEventListener('DOMContentLoaded', function() {
    function populateDropdown(url, dropdownId) {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const dropdown = document.getElementById(dropdownId);
                dropdown.innerHTML = ''; // clear existing options
                data.forEach(item => {
                    const option = document.createElement('option');
                    option.value = item.id;
                    option.textContent = item.name;
                    dropdown.appendChild(option);
                });
            });
    }

    // populate movement dropdowns
    populateDropdown('/api/get_movements', 'deleteMovementId');
    populateDropdown('/api/get_movements', 'addMovementTagMovementId');

    // populate tag dropdowns
    populateDropdown('/api/get_tags', 'deleteTagId');
    populateDropdown('/api/get_tags', 'addMovementTagTagId');

    document.getElementById('addMovementForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        fetch('/add_movement', {
            method: 'POST',
            body: formData
        }).then(response => response.text()).then(data => alert(data));
    });

    document.getElementById('deleteMovementForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const movementId = document.getElementById('deleteMovementId').value;
        fetch('/delete_movement', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ movement_id: movementId }),
        }).then(response => response.text()).then(data => alert(data));
    });

    document.getElementById('addTagForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        fetch('/add_tag', {
            method: 'POST',
            body: formData
        }).then(response => response.text()).then(data => alert(data));
    });

    document.getElementById('deleteTagForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const tagId = document.getElementById('deleteTagId').value;
        fetch('/delete_tag', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ tag_id: tagId }),
        }).then(response => response.text()).then(data => alert(data));
    });

    document.getElementById('addMovementTagForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const movementId = document.getElementById('addMovementTagMovementId').value;
        const tagId = document.getElementById('addMovementTagTagId').value;
        const value = document.getElementById('value').value;

        console.log(JSON.stringify({ movement_id: movementId, tag_id: tagId, value }))

        fetch('/add_movement_tag', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ movement_id: movementId, tag_id: tagId, value }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Movement Tag added successfully');
            } else {
                alert('Failed to add Movement Tag');
            }
        });
    });


    document.getElementById('getMovementsButton').addEventListener('click', (event)=> {
        event.preventDefault();
        fetch('/get_movements', {
            method: 'GET'
        }).then(response => response.text()).then(data => alert(data));
    });
});
