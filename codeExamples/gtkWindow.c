// http://zetcode.com/gui/gtk2/gtkevents/

#include <gtk/gtk.h>

static void on_window_closed (GtkWidget *widget, gpointer data)
{
    g_print("Aus die Maus\n");
    gtk_main_quit ();
}

int main(int argc, char *argv[]) {

  GtkWidget *window;
  gtk_init(&argc, &argv);

  window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
  gtk_window_set_title(GTK_WINDOW(window), "Erstes GUI Window");

  g_signal_connect(G_OBJECT(window), "destroy",
      G_CALLBACK(on_window_closed), NULL);

  gtk_widget_show_all(window);

  gtk_main();

  return 0;
}
