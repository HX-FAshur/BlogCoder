# BlogEntregaFinal
El sitio creado es un blog de diseño minimalista, estilizado en forma básica con bootstrap. En el landing, permite visualizar los posts en forma de tarjetas con snippets, indicando ademas quién es el autor de cada post. Puede accederse al mismo en [BlogCoder](https://blog-coder-far.herokuapp.com/).  
En el navbar se brinda la posibilidad de registrarse y de hacer login.  
  
![imagen](https://user-images.githubusercontent.com/49619096/178545525-ba2acfce-cfcd-41f7-a4c2-90797b2a46ee.png)

<ins><b>Registro</b></ins>  
La pagina de registro pide datos basicos para crear un usuario, brindando recomendaciones de seguridad para la creacion de contraseñas. Finalizado el registro, se redirige a la pagina de login.  
  
![imagen](https://user-images.githubusercontent.com/49619096/178545640-62f66081-8bb3-4f97-bece-9e01b6fe3f38.png)

<ins><b>Login</b></ins>  
Cuando se realiza el login, se redirige a la pagina de inicio cuyo navbar ahora muestra opciones de Creacion de posts, Gestion de usuario y logout.  
  
![imagen](https://user-images.githubusercontent.com/49619096/178543964-c097b3b1-6ae0-41d8-b44c-a707dd6d26f4.png)  
  
  <ins><b>Gestion de Usuario</b></ins>  
  El menu de Usuario mostrará por defecto la opcion de editar datos de usuario y de crear un Perfil en el caso de que el usuario no lo tenga ya. Si el usuario posee un perfil, entonces el menu mostrará las opciones de Editar Perfil y Ver Perfil.  
  
![imagen](https://user-images.githubusercontent.com/49619096/178545825-2681563d-6fc3-45fd-8ce4-258e30d6213c.png)  
  
  <hr>  
  
<ins><b>Seguridad</b></ins>  
Para la edicion y eliminacion de posts se realiza una verificacion para asegurar que cada usuario solo pueda modificar sus propios posts. En caso de que un usuario quiera editar o borrar un post ajeno utilizando como atajo la ruta (por ejemplo: /article/edit/<article_id>/delete), se le indicará que está accediendo a un Area Restringida y que solicite permiso al autor para la accion que intenta realizar.  

<hr>  

Para su funcionamiento, el sitio consta actualmente de dos aplicaciones: Blog y users.
- 'Blog' maneja todo el core del blog en sí: creación, edición y borrado de posts como así también su visualizacion.
  Mediante el módulo 'ckeditor', la página de creación/edición de posts permite añadir formato e imágenes embebidas mediante links a los posts. Además, se incluyó la posibilidad de subir imágenes desde archivos.
- 'users' administra y permite registrar usuarios, hacer login/logout y ver/editar páginas de perfil para la visualizacion de los datos de cada usuario re gistrado. El registro y posterior login permite a los usuarios crear y borrar posts en el blog y gestionar sus páginas de perfil.
