document.addEventListener("DOMContentLoaded", () => {
    const placeList = document.getElementById("placeList");
    const placeForm = document.getElementById("placeForm");
    const deleteForm = document.getElementById("deleteForm");

    function loadPlace() {
        fetch("/api/places")
            .then(response => response.json())
            .then(places => {
                placeList.innerHTML = "";
                places.forEach(place => {
                    const li = document.createElement("li");
                    li.innerHTML = `${place.company} ${place.term}`;
                    placeList.appendChild(li);
                });
            });
    }

    placeForm.addEventListener("submit", event => {
        event.preventDefault();
        const company = document.getElementById("company").value;
        const term = document.getElementById("term").value;

        fetch("/api/places", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ company, term })
        }).then(response => response.json())
          .then(() => {
                placeForm.reset();
                loadPlace();
            });
    });

    
    deleteForm.addEventListener('delete', (e) => {
        e.preventDefault();
        e.target.reset(); 
    });

    // loadPlace();

});