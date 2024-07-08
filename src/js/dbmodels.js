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

    function populateDropdowns() {
        // populate movement dropdowns
        populateDropdown('/api/get_movements', 'deleteMovementId');
        populateDropdown('/api/get_movements', 'addMovementTagMovementId');

        // populate tag dropdowns
        populateDropdown('/api/get_tags', 'deleteTagId');
        populateDropdown('/api/get_tags', 'addMovementTagTagId');
    }

    populateDropdowns();

    document.getElementById('addMovementForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        fetch('/add_movement', {
            method: 'POST',
            body: formData
        //}).then(response => response.text()).then(data => alert(data));
        }).then(response => response.text()).then(data => data);
        main();
        populateDropdowns();
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
        }).then(response => response.text()).then(data => data);
        main();
        populateDropdowns();
    });

    document.getElementById('addTagForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        fetch('/add_tag', {
            method: 'POST',
            body: formData
        }).then(response => response.text()).then(data => data);
        main();
        populateDropdowns();
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
        }).then(response => response.text()).then(data => data);
        main();
        populateDropdowns();
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
        main();
        populateDropdowns();
    });


});

async function printMovementTable(movements) {
    // make movements alphabetical
    movements.sort((a, b) => a.name.localeCompare(b.name));

    //const tableContainer = document.getElementById("databaseTable");
    //const tableContainer = document.getElementById("databaseContainer");
    const topTableRow = document.getElementById('topTableRow');
    const topTableData = document.createElement('td');
    const tableElement = document.createElement('table');
    tableElement.classList.add('table', 'table-hover');
    
    // create table header
    header = document.createElement('thead');
    headerRow = document.createElement('tr');
    headerTitle = document.createElement('th');
    headerTitle.innerHTML = `<strong>Movement<strong>`;
    headerRow.appendChild(headerTitle);
    header.appendChild(headerRow);
    tableElement.appendChild(header);

    // create and populate table body
    const body = document.createElement('tbody');
    movements.forEach(movement => {
        const movementRow = document.createElement('tr');
        const movementName = document.createElement('td');
        movementName.innerHTML = `${movement.name}`;
        movementRow.appendChild(movementName);
        body.appendChild(movementRow);
    });

    tableElement.appendChild(body);
    //tableContainer.appendChild(tableElement);
    topTableData.appendChild(tableElement);
    topTableRow.appendChild(topTableData);
}


async function fetchMovements() {
    let sqlMovements = [];
    const response = await fetch('/api/get_movements');
    const data = await response.json();
        data.forEach(item => {
            movementName = item.name;
            let movementObject = {
                "name": movementName
            };
            sqlMovements.push(movementObject);
        });
    return sqlMovements;
}

async function main() {
    const pythonMovements = window.pythonMovements;
    let sqlMovements = await fetchMovements();
    const topTableRow = document.getElementById('topTableRow');
    topTableRow.innerHTML = ``;
    console.log(pythonMovements);
    console.log(sqlMovements);
    printMovementTable(pythonMovements);
    printMovementTable(sqlMovements);
}

main();
