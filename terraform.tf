resource "local_file" "productos" {
    content= "listado de productos"
    filename= "productos-${random_pet.sufijo.id}.txt"
}

resource "random_pet" "sufijo" {
}