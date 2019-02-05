#include <gtk/gtk.h>

static int counter = 0;

void greet( GtkWidget *widget, gpointer data ){
   g_print ("%s clicked %d times\n",
      (char*)data, ++counter);
}

static void on_window_closed (GtkWidget *widget, gpointer data){
    g_print("Aus die Maus\n");
    gtk_main_quit ();
}

int main(int argc, char *argv[]) {

  GtkWidget *window;
  gtk_init(&argc, &argv);

  window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
  gtk_window_set_title(GTK_WINDOW(window), "Erstes GUI Window");
  gtk_window_set_default_size(GTK_WINDOW(window), 300, 200);
  gtk_container_set_border_width(GTK_CONTAINER(window), 15);

  GtkWidget *halign;
  halign = gtk_alignment_new(0, 0, 0, 0);

  GtkWidget *button;
  button = gtk_button_new_with_label ("Click Me!");
  g_signal_connect (GTK_OBJECT(button),
     "clicked",G_CALLBACK (greet),
     "button");

  gtk_container_add(GTK_CONTAINER(halign), button);
  gtk_container_add(GTK_CONTAINER(window), halign);

  g_signal_connect(G_OBJECT(window), "destroy",
      G_CALLBACK(on_window_closed), NULL);

  gtk_widget_show_all(window);

  gtk_main();

  return 0;
}
