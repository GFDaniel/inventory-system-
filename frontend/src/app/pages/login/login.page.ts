import { Component, OnInit } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { Router } from "@angular/router";
import { LoadingController, AlertController } from "@ionic/angular";
import { AuthService } from "../../services/auth.service";

@Component({
  selector: "app-login",
  templateUrl: "./login.page.html",
  styleUrls: ["./login.page.scss"],
})
export class LoginPage implements OnInit {
  loginForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private router: Router,
    private loadingController: LoadingController,
    private alertController: AlertController
  ) {
    this.loginForm = this.formBuilder.group({
      username: ["", [Validators.required]],
      password: ["", [Validators.required]],
    });
  }

  ngOnInit() {
    // Si ya está autenticado, redirigir a tabs
    if (this.authService.isAuthenticated()) {
      this.router.navigate(["/tabs"]);
    }
  }

  async onSubmit() {
    if (this.loginForm.valid) {
      const loading = await this.loadingController.create({
        message: "Iniciando sesión...",
      });
      await loading.present();

      this.authService.login(this.loginForm.value).subscribe({
        next: async (response) => {
          await loading.dismiss();
          this.router.navigate(["/tabs"]);
        },
        error: async (error) => {
          await loading.dismiss();
          const alert = await this.alertController.create({
            header: "Error",
            message: error.error?.error || "Error al iniciar sesión",
            buttons: ["OK"],
          });
          await alert.present();
        },
      });
    }
  }
}

export default LoginPage;
