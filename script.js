document.addEventListener("DOMContentLoaded", function () {
    const activityTree = document.getElementById("activity-tree");

    // Получаем данные из параметров URL
    const urlParams = new URLSearchParams(window.location.search);
    const activityData = JSON.parse(urlParams.get("activity"));

    // Функция для создания дерева активности
    function createActivityTree(data) {
        const tree = document.createElement("ul");
        tree.classList.add("activity-tree");

        data.forEach(event => {
            const eventItem = document.createElement("li");
            eventItem.classList.add("event-item");

            const eventType = document.createElement("div");
            eventType.classList.add("event-type");
            eventType.textContent = event.type;
            eventItem.appendChild(eventType);

            const eventDetails = document.createElement("div");
            eventDetails.classList.add("event-details");
            eventDetails.textContent = `Repo: ${event.repo.name}, Date: ${new Date(event.created_at).toLocaleDateString()}`;
            eventItem.appendChild(eventDetails);

            tree.appendChild(eventItem);
        });

        return tree;
    }

    // Отображение дерева активности
    if (activityData) {
        const tree = createActivityTree(activityData);
        activityTree.appendChild(tree);
    } else {
        activityTree.textContent = "Нет данных для отображения.";
    }
});
