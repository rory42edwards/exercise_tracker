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

        fetch('/add_movement_tag', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ movement_id: movementId, tag_id: tagId, value }),
        })
        .then(response => response.json())
        .then(data => data);
        main();
        populateDropdowns();
    });

    document.getElementById('deleteMovementTagForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const movementId = document.getElementById('addMovementTagMovementId').value;
        const tagId = document.getElementById('addMovementTagTagId').value;
        const value = document.getElementById('value').value;

        fetch('/delete_movement_tag', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ movement_id: movementId, tag_id: tagId, value }),
        })
        .then(response => response.json())
        .then(data => data);
        main();
        populateDropdowns();
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

    async function printTagTable(tags) {
        // make tags alphabetical
        tags.sort((a, b) => a.name.localeCompare(b.name));

        const topTableRow = document.getElementById('topTagsTableRow');
        const topTableData = document.createElement('td');
        const tableElement = document.createElement('table');
        tableElement.classList.add('table', 'table-hover');
        
        // create table header
        header = document.createElement('thead');
        headerRow = document.createElement('tr');
        headerTitle = document.createElement('th');
        headerTitle.innerHTML = `<strong>Tags<strong>`;
        headerRow.appendChild(headerTitle);
        header.appendChild(headerRow);
        tableElement.appendChild(header);

        // create and populate table body
        const body = document.createElement('tbody');
        tags.forEach(tag => {
            const tagRow = document.createElement('tr');
            const tagName = document.createElement('td');
            tagName.innerHTML = `${tag.name}`;
            tagRow.appendChild(tagName);
            body.appendChild(tagRow);
        });

        tableElement.appendChild(body);
        topTableData.appendChild(tableElement);
        topTableRow.appendChild(topTableData);
    }

    async function printMovementTagTable(movementTags) {
        // extract all unique tags and put into a sorted array
        const allTags = new Set();
        movementTags.forEach(movement => {
            Object.keys(movement.tags).forEach(tag => allTags.add(tag));
        });
        const tagsArray = Array.from(allTags).sort();

        // create table
        const table = document.getElementById('databaseMovementTagsTable');
        table.innerHTML = ``;
        table.border = '1';

        const header = document.createElement('thead');
        const headerRow = document.createElement('tr');
        const firstCell = document.createElement('th');
        firstCell.innerHTML = `<strong>Movements</strong>`;
        headerRow.appendChild(firstCell);
        tagsArray.forEach(tag => {
            const th = document.createElement('th');
            th.textContent = tag;
            headerRow.appendChild(th);
        });
        header.appendChild(headerRow);
        table.appendChild(header);

        // create and fill table rows
        const body = document.createElement('tbody');
        movementTags.forEach(movement => {
            const row = document.createElement('tr');
            const movementCell = document.createElement('td');
            movementCell.textContent = movement.name;
            row.appendChild(movementCell);

            tagsArray.forEach(tag => {
                const cell = document.createElement('td');
                cell.textContent = movement.tags[tag] || '';
                row.appendChild(cell);
            });

            body.appendChild(row);
        });
        table.appendChild(body);
    }

    async function fetchDbDataNames(url) {
        let dbData = [];
        const response = await fetch(url);
        const data = await response.json();
        data.forEach(item => {
            dataName = item.name;
            let dataObject = {
                "name": dataName
            };
            dbData.push(dataObject);
        });
        return dbData;
    }

    async function fetchDbMovementTags() {
        const response = await fetch('/api/get_combined_data');
        const data = await response.json();
        return data;
    }

    async function main() {
        const pythonMovements = window.pythonMovements;
        let sqlMovements = await fetchDbDataNames('/api/get_movements');
        let sqlTags = await fetchDbDataNames('/api/get_tags');
        let sqlMovementTags = await fetchDbMovementTags();
        const topTableRow = document.getElementById('topTableRow');
        topTableRow.innerHTML = ``;
        printMovementTable(pythonMovements);
        printMovementTable(sqlMovements);
        printTagTable(sqlTags);
        printMovementTagTable(sqlMovementTags);
    }

    main();
});
