import { Component, OnInit } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { AlertController, LoadingController } from "@ionic/angular";
import { InventoryMovementService } from "../../services/inventory-movement.service";
import { ProductService } from "../../services/product.service";
import { InventoryMovement } from "../../models/inventory-movement.model";
import { Product } from "../../models/product.model";

@Component({
  selector: "app-movements",
  templateUrl: "./movements.page.html",
  styleUrls: ["./movements.page.scss"],
})
export class MovementsPage implements OnInit {
  movements: InventoryMovement[] = [];
  products: Product[] = [];
  movementForm: FormGroup;
  selectedProduct: Product | null = null;

  constructor(
    private movementService: InventoryMovementService,
    private productService: ProductService,
    private formBuilder: FormBuilder,
    private alertController: AlertController,
    private loadingController: LoadingController
  ) {
    this.movementForm = this.formBuilder.group({
      product: ["", [Validators.required]],
      movement_type: ["", [Validators.required]],
      quantity: ["", [Validators.required, Validators.min(1)]],
      description: [""],
    });
  }

  ngOnInit() {
    this.loadProducts();
    this.loadMovements();
  }

  async loadProducts() {
    this.productService.getProducts().subscribe({
      next: (products) => {
        this.products = products;
      },
      error: (error) => {
        console.error("Error loading products:", error);
      },
    });
  }

  async loadMovements() {
    const loading = await this.loadingController.create({
      message: "Cargando movimientos...",
    });
    await loading.present();

    this.movementService.getMovements().subscribe({
      next: (movements) => {
        this.movements = movements;
        loading.dismiss();
      },
      error: (error) => {
        console.error("Error loading movements:", error);
        loading.dismiss();
      },
    });
  }

  onProductChange() {
    const productId = this.movementForm.get("product")?.value;
    this.selectedProduct =
      this.products.find((p) => p.id === Number.parseInt(productId)) || null;
  }

  async onSubmit() {
    if (this.movementForm.valid) {
      const movementData = this.movementForm.value;

      // Validar stock para salidas
      if (movementData.movement_type === "OUT" && this.selectedProduct) {
        if (movementData.quantity > this.selectedProduct.stock) {
          const alert = await this.alertController.create({
            header: "Error",
            message: `No hay suficiente stock. Stock disponible: ${this.selectedProduct.stock}`,
            buttons: ["OK"],
          });
          await alert.present();
          return;
        }
      }

      const loading = await this.loadingController.create({
        message: "Registrando movimiento...",
      });
      await loading.present();

      this.movementService.createMovement(movementData).subscribe({
        next: () => {
          loading.dismiss();
          this.movementForm.reset();
          this.selectedProduct = null;
          this.loadMovements();
          this.loadProducts(); // Recargar para actualizar stock
          this.showSuccessAlert("Movimiento registrado exitosamente");
        },
        error: (error) => {
          loading.dismiss();
          const errorMessage =
            error.error?.non_field_errors?.[0] ||
            "Error al registrar el movimiento";
          this.showErrorAlert(errorMessage);
        },
      });
    }
  }

  getMovementTypeText(type: string): string {
    return type === "IN" ? "Entrada" : "Salida";
  }

  getMovementTypeColor(type: string): string {
    return type === "IN" ? "success" : "warning";
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

export default MovementsPage;
