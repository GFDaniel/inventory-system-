import { Component, OnInit } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import {
  AlertController,
  LoadingController,
  ModalController,
} from "@ionic/angular";
import { ProductService } from "../../services/product.service";
import { Product } from "../../models/product.model";

@Component({
  selector: "app-products",
  templateUrl: "./products.page.html",
  styleUrls: ["./products.page.scss"],
})
export class ProductsPage implements OnInit {
  products: Product[] = [];
  productForm: FormGroup;
  isEditing = false;
  editingProductId: number | null = null;

  constructor(
    private productService: ProductService,
    private formBuilder: FormBuilder,
    private alertController: AlertController,
    private loadingController: LoadingController,
    private modalController: ModalController
  ) {
    this.productForm = this.formBuilder.group({
      name: ["", [Validators.required]],
      description: [""],
      price: ["", [Validators.required, Validators.min(0)]],
      stock: ["", [Validators.required, Validators.min(0)]],
    });
  }

  ngOnInit() {
    this.loadProducts();
  }

  async loadProducts() {
    const loading = await this.loadingController.create({
      message: "Cargando productos...",
    });
    await loading.present();

    this.productService.getProducts().subscribe({
      next: (products) => {
        this.products = products;
        loading.dismiss();
      },
      error: (error) => {
        console.error("Error loading products:", error);
        loading.dismiss();
      },
    });
  }

  async onSubmit() {
    if (this.productForm.valid) {
      const loading = await this.loadingController.create({
        message: this.isEditing
          ? "Actualizando producto..."
          : "Creando producto...",
      });
      await loading.present();

      const productData = this.productForm.value;

      if (this.isEditing && this.editingProductId) {
        this.productService
          .updateProduct(this.editingProductId, productData)
          .subscribe({
            next: () => {
              loading.dismiss();
              this.resetForm();
              this.loadProducts();
              this.showSuccessAlert("Producto actualizado exitosamente");
            },
            error: (error) => {
              loading.dismiss();
              this.showErrorAlert("Error al actualizar el producto");
            },
          });
      } else {
        this.productService.createProduct(productData).subscribe({
          next: () => {
            loading.dismiss();
            this.resetForm();
            this.loadProducts();
            this.showSuccessAlert("Producto creado exitosamente");
          },
          error: (error) => {
            loading.dismiss();
            this.showErrorAlert("Error al crear el producto");
          },
        });
      }
    }
  }

  editProduct(product: Product) {
    this.isEditing = true;
    this.editingProductId = product.id!;
    this.productForm.patchValue(product);
  }

  async deleteProduct(product: Product) {
    const alert = await this.alertController.create({
      header: "Confirmar eliminación",
      message: `¿Estás seguro de que deseas eliminar el producto "${product.name}"?`,
      buttons: [
        {
          text: "Cancelar",
          role: "cancel",
        },
        {
          text: "Eliminar",
          handler: () => {
            this.confirmDelete(product.id!);
          },
        },
      ],
    });
    await alert.present();
  }

  async confirmDelete(productId: number) {
    const loading = await this.loadingController.create({
      message: "Eliminando producto...",
    });
    await loading.present();

    this.productService.deleteProduct(productId).subscribe({
      next: () => {
        loading.dismiss();
        this.loadProducts();
        this.showSuccessAlert("Producto eliminado exitosamente");
      },
      error: (error) => {
        loading.dismiss();
        this.showErrorAlert("Error al eliminar el producto");
      },
    });
  }

  resetForm() {
    this.productForm.reset();
    this.isEditing = false;
    this.editingProductId = null;
  }

  async showSuccessAlert(message: string) {
    const alert = await this.alertController.create({
      header: "Éxito",
      message: message,
      buttons: ["OK"],
    });
    await alert.present();
  }

  async showErrorAlert(message: string) {
    const alert = await this.alertController.create({
      header: "Error",
      message: message,
      buttons: ["OK"],
    });
    await alert.present();
  }
}

export default ProductsPage;
