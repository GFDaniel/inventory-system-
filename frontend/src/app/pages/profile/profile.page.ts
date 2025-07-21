import { Component, type OnInit } from "@angular/core";
import { Router } from "@angular/router";
import { AlertController } from "@ionic/angular";
import { AuthService } from "../../services/auth.service";
import { User } from "../../models/user.model";

@Component({
  selector: "app-profile",
  templateUrl: "./profile.page.html",
  styleUrls: ["./profile.page.scss"],
})
export class ProfilePage implements OnInit {
  user: User | null = null;

  constructor(
    private authService: AuthService,
    private router: Router,
    private alertController: AlertController
  ) {}

  ngOnInit() {
    this.user = this.authService.getCurrentUser();
  }

  async logout() {
    const alert = await this.alertController.create({
      header: "Cerrar Sesión",
      message: "¿Estás seguro de que deseas cerrar sesión?",
      buttons: [
        {
          text: "Cancelar",
          role: "cancel",
        },
        {
          text: "Cerrar Sesión",
          handler: () => {
            this.authService.logout();
            this.router.navigate(["/login"]);
          },
        },
      ],
    });
    await alert.present();
  }
}

export default ProfilePage;
