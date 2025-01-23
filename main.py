<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Образовательный Портал</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
        }
        .navbar {
            background-color: #1e1e1e;
        }
        .card {
            background-color: #1e1e1e;
            color: #e0e0e0;
            transition: transform 0.2s;
        }
        .card:hover {
            transform: scale(1.05);
        }
        .card-body {
            background-color: #2b2b2b;
            border-radius: 10px;
        }
        .welcome-section {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            max-height: 50vh;
        }
        .button-column {
            display: flex;
            flex-direction: column;
            margin-left: 20px;
        }
        footer {
            text-align: center;
            padding: 20px;
            background-color: #1e1e1e;
            position: relative;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="#">Образовательный Портал</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#courses">Курсы</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#solution">Решение</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <main class="container my-5">
        <div class="welcome-section my-4">
            <div>
                <h1>Добро пожаловать!</h1>
                <h2>Наш образовательный ресурс. Он создан для подготовки к экзаменам. Надеюсь, вы сочтете его полезным.</h2>
            </div>
            <div class="button-column">
                <a href="#courses" class="btn btn-primary mb-2 btn-lg">Курсы</a>
                <a href="#solution" class="btn btn-primary mb-2 btn-lg">Решение</a>
            </div>
        </div>
        <section id="courses" class="my-5">
            <h2 class="text-center">Курсы</h2>
            <div class="row">
                <div class="col-md-4">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h3>Курс 1</h3>
                            <p>Описание курса 1.</p>
                            <button class="btn btn-primary">Перейти к курсу</button>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h3>Курс 2</h3>
                            <p>Описание курса 2.</p>
                            <button class="btn btn-primary">Перейти к курсу</button>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h3>Курс 3</h3>
                            <p>Описание курса 3.</p>
                            <button class="btn btn-primary">Перейти к курсу</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="solution" class="my-5">
            <h2 class="text-center">Решение</h2>
            <div class="row">
                <div class="col-md-6">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h3>Тест</h3>
                            <p>Описание теста.</p>
                            <button class="btn btn-primary">Начать тест</button>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h3>Задачи</h3>
                            <p>Описание задач.</p>
                            <button class="btn btn-primary">Перейти к задачам</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <p>© 2023 Образовательный Портал. Все права защищены.</p>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.min.js"></script>
</body>
</html>