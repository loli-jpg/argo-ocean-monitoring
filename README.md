# argo-ocean-monitoring

Прогнозно-аналитическая система мониторинга состояния Мирового океана на данных программы Argo.

## Источники данных
- Статический датасет: [Otter21/ARGO_Profiles](https://huggingface.co/datasets/Otter21/ARGO_Profiles)
- Динамический API: [Argovis API](https://argovis-api.colorado.edu/docs/)

## Структура проекта
argo-ocean-monitoring/
├── config/ # Конфигурация
├── data/
│ ├── raw/ # Сырые данные
│ ├── processed/ # Очищенные данные
│ └── mart/ # Аналитические витрины
├── docs/ # Документация
├── logs/ # Журналы загрузок
├── notebooks/ # Jupyter-ноутбуки
├── src/
│ ├── ingestion/ # Загрузка данных
│ ├── processing/ # Обработка
│ ├── quality/ # Контроль качества
│ ├── models/ # Модели прогноза
│ └── visualization/# Визуализация
└── tests/ # Тесты