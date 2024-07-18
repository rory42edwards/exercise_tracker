import { fetchExerciseLoadData, fetchExerciseLoadVolumeData, fetchProgressiveOverloadData } from './api.js';
import { updateChart, createTimeChart } from './mychart.js';
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
                    option.setAttribute('data-exercise', item.name);
                    dropdown.appendChild(option);
                });
            });
    }

function populateDropdowns() {
        // populate movement dropdowns
        populateDropdown('/api/get_movements', 'movementId');
    }

export function renderMovements() {
    const header = document.createElement('h2');
    header.innerHTML = `Analysis`;
    const pythonMovements = window.pythonMovements;
    const container = document.getElementById('analysisContainer');
    container.setAttribute('style','width: 800px;');
    container.innerHTML = '';
    container.appendChild(header);

    const movementForm = document.createElement('form');
    movementForm.setAttribute('id', 'movementForm');
    const movementLabel = document.createElement('label');
    movementLabel.setAttribute('for','movementId');
    movementLabel.innerText = 'Select movement: ';
    const movementSelect = document.createElement('select');
    movementSelect.setAttribute('id','movementId');
    movementSelect.setAttribute('name','movementId');
    movementForm.appendChild(movementLabel);
    movementForm.appendChild(movementSelect);
    const plotInput = document.createElement('input');
    plotInput.setAttribute('type', 'submit');
    plotInput.setAttribute('value', 'PLOT');
    //plotInput.setAttribute('class', 'plot-load-button');
    movementForm.appendChild(plotInput);
    container.appendChild(movementForm);

    populateDropdowns();

    

    /*
    pythonMovements.forEach(movement => {
        const plotMovementButton = document.createElement('button');
        const buttonId = movement.name.concat('Button');
        plotMovementButton.setAttribute('id', buttonId);
        plotMovementButton.setAttribute('class', 'plot-load-button');
        plotMovementButton.setAttribute('data-exercise', movement.name);
        plotMovementButton.innerText = `Plot Load: ${movement.name}`;

        //plotMovementDiv.appendChild(plotMovementButton);
        container.appendChild(plotMovementButton);
    });
    */
}
