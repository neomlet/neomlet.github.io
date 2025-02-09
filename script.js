document.addEventListener("DOMContentLoaded", function () {
    const activityTree = document.getElementById("activity-tree");

    // Получаем ключ из параметров URL
    const urlParams = new URLSearchParams(window.location.search);
    const activityKey = urlParams.get("key");

    // Получаем данные активности по ключу
    if (activityKey) {
        fetch(`/api/get_activity?key=${activityKey}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Ошибка при получении данных");
                }
                return response.json();
            })
            .then(activityData => {
                if (activityData && !activityData.error) {
                    const tree = createActivityTree(activityData);
                    activityTree.appendChild(tree);
                } else {
                    activityTree.textContent = "Нет данных для отображения.";
                }
            })
            .catch(error => {
                console.error("Ошибка при получении данных:", error);
                activityTree.textContent = "Произошла ошибка при загрузке данных.";
            });
    } else {
        activityTree.textContent = "Ключ активности не указан.";
    }

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
});
