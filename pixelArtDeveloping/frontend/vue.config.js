const static_dir = "../static";
// Путь, относительно static_dir
// В него webpack положит шаблон Vue приложения
const template_path = "../templates/index.html";

module.exports = {
  // Paths
  // Рабочая директория сборки
  // Я обычно указываю директорию приложения django, которое отвеает за фронт
  outputDir: process.env.NODE_ENV === "production" ? static_dir : "dist/",
  // Куда пойдёт шаблон проекта
  indexPath:
    process.env.NODE_ENV === "production" ? template_path : "index.html",
  // Куда пойдут ассеты (относительно outputDir)
  assetsDir: "", // ассеты храним там же, где и JS/CSS
  // Путь по которому можно достать статику
  // Нужно указать тот, который прописан в STATIC_URL настроек django
  publicPath: process.env.NODE_ENV === "production" ? "static" : "/",
};
