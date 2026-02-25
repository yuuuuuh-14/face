import { Component, signal, inject, effect } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatListModule } from '@angular/material/list';
import { MatDialogModule, MatDialog } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { DashboardService, Face, Log } from './dashboard.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatToolbarModule,
    MatButtonModule,
    MatIconModule,
    MatCardModule,
    MatProgressBarModule,
    MatListModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule
  ],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  private dashboardService = inject(DashboardService);
  private dialog = inject(MatDialog);

  faces = this.dashboardService.faces;
  registeredNames = this.dashboardService.registeredNames;
  logs = this.dashboardService.logs;
  accessHistory = this.dashboardService.accessHistory;
  systemStatus = this.dashboardService.systemStatus;
  uptime = this.dashboardService.uptime;

  showRegisterModal = signal(false);
  newName = signal('');
  isRegistering = signal(false);

  metrics = [
    { label: 'Neural Process', value: 88, icon: 'bolt' },
    { label: 'Latency', value: 12, icon: 'speed' },
    { label: 'Memory Usage', value: 45, icon: 'layers' }
  ];

  constructor() {
    // Log connection status
    effect(() => {
      console.log('System Status:', this.systemStatus());
    });
  }

  getBBoxStyle(face: Face) {
    const isUnknown = face.name === 'UNKNOWN';
    const color = isUnknown ? '#ef4444' : '#10b981';

    return {
      position: 'absolute',
      left: `${(face.bbox[0] / 640) * 100}%`,
      top: `${(face.bbox[1] / 640) * 100}%`,
      width: `${((face.bbox[2] - face.bbox[0]) / 640) * 100}%`,
      height: `${((face.bbox[3] - face.bbox[1]) / 640) * 100}%`,
      border: `2px solid ${color}`,
      'box-shadow': `0 0 15px ${color}80`,
      zIndex: 20
    };
  }

  openRegister() {
    this.showRegisterModal.set(true);
  }

  closeRegister() {
    this.showRegisterModal.set(false);
    this.newName.set('');
  }

  handleRegister() {
    const name = this.newName().trim();
    if (!name) return;

    this.isRegistering.set(true);
    this.dashboardService.registerFace(name).subscribe({
      next: (res) => {
        if (res.success) {
          this.dashboardService.addLog(`[SYSTEM] Subject '${name}' registered successfully`, 'info');
          this.dashboardService.fetchRegisteredFaces();
          this.closeRegister();
        } else {
          alert(res.message);
        }
        this.isRegistering.set(false);
      },
      error: () => {
        alert('Error during registration.');
        this.isRegistering.set(false);
      }
    });
  }

  handleDelete(name: string) {
    if (!confirm(`Are you sure you want to remove '${name}' from registry?`)) return;

    this.dashboardService.deleteFace(name).subscribe({
      next: (res) => {
        if (res.success) {
          this.dashboardService.addLog(`[SYSTEM] Subject '${name}' removed`, 'warning');
          this.dashboardService.fetchRegisteredFaces();
        } else {
          alert(res.message);
        }
      },
      error: () => alert('Error deleting subject.')
    });
  }
}
