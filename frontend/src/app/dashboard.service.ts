import { Injectable, signal, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

export interface Face {
    bbox: number[];
    name: string;
    score: number;
    match_score: number;
    gender: string;
    age: number;
    liveness: string;
}

export interface Log {
    id: number;
    text: string;
    time: string;
    type: 'info' | 'success' | 'warning' | 'error';
}

export interface AccessLog {
    id: number;
    name: string;
    timestamp: string;
    liveness: string;
}

@Injectable({
    providedIn: 'root'
})
export class DashboardService implements OnDestroy {
    private apiUrl = environment.apiUrl;
    private eventSource: EventSource | null = null;
    private logPollingInterval: any;

    // Signals for reactive state
    faces = signal<Face[]>([]);
    registeredNames = signal<string[]>([]);
    logs = signal<Log[]>([]);
    accessHistory = signal<AccessLog[]>([]);
    systemStatus = signal<'ONLINE' | 'OFFLINE'>('OFFLINE');
    uptime = signal<string>('00:00:00');

    constructor(private http: HttpClient) {
        this.initializeSSE();
        this.fetchRegisteredFaces();
        this.startUptimeCounter();
        this.startAccessLogPolling();
    }

    private initializeSSE() {
        if (this.eventSource) {
            this.eventSource.close();
        }

        this.eventSource = new EventSource(`${this.apiUrl}/stream/events`);

        this.eventSource.onopen = () => {
            this.systemStatus.set('ONLINE');
            this.addLog('[SYSTEM] SSE connection established', 'info');
        };

        this.eventSource.onmessage = (event) => {
            try {
                const data = JSON.parse(event.data);
                if (data.faces) {
                    this.faces.set(data.faces);
                    this.processAnalysisResults(data.faces);
                }
            } catch (err) {
                console.error('Failed to parse SSE data:', err);
            }
        };

        this.eventSource.onerror = (err) => {
            console.error('SSE connection error:', err);
            this.systemStatus.set('OFFLINE');
            this.faces.set([]);
            // Basic retry logic is handled by EventSource automatically
        };
    }

    private processAnalysisResults(faces: Face[]) {
        faces.forEach(face => {
            if (face.name !== 'UNKNOWN') {
                const currentLogs = this.logs();
                // Avoid flooding logs with the same detection within a short window
                const lastLog = currentLogs[0];
                const isDuplicate = lastLog && lastLog.text.includes(face.name) &&
                    (Date.now() - lastLog.id < 5000);

                if (!isDuplicate) {
                    this.addLog(`[DETECT] ${face.name} (Match: ${(face.match_score * 100).toFixed(0)}%)`, 'success');
                }
            }
        });
    }

    fetchRegisteredFaces() {
        this.http.get<{ success: boolean; names: string[] }>(`${this.apiUrl}/face/`).subscribe({
            next: (data) => {
                if (data.success) {
                    this.registeredNames.set(data.names || []);
                }
            },
            error: (err) => console.error('Failed to load registered faces:', err)
        });
    }

    registerFace(name: string): Observable<{ success: boolean; message: string }> {
        return this.http.post<{ success: boolean; message: string }>(`${this.apiUrl}/face/register`, { name });
    }

    deleteFace(name: string): Observable<{ success: boolean; message: string }> {
        return this.http.delete<{ success: boolean; message: string }>(`${this.apiUrl}/face/${name}`);
    }

    addLog(text: string, type: Log['type'] = 'info') {
        const newLog: Log = {
            id: Date.now(),
            text,
            time: new Date().toLocaleTimeString(),
            type
        };
        this.logs.update(prev => [newLog, ...prev].slice(0, 50));
    }

    fetchAccessLogs() {
        this.http.get<{ success: boolean; logs: AccessLog[] }>(`${this.apiUrl}/logs/?limit=50`).subscribe({
            next: (data) => {
                if (data.success) {
                    this.accessHistory.set(data.logs || []);
                }
            },
            error: (err) => console.error('Failed to load access logs:', err)
        });
    }

    private startAccessLogPolling() {
        this.fetchAccessLogs(); // Initial fetch
        this.logPollingInterval = setInterval(() => {
            this.fetchAccessLogs();
        }, 5000); // Poll every 5 seconds
    }

    private startUptimeCounter() {
        const startTime = Date.now();
        setInterval(() => {
            const elapsed = Date.now() - startTime;
            const h = Math.floor(elapsed / 3600000).toString().padStart(2, '0');
            const m = Math.floor((elapsed % 3600000) / 60000).toString().padStart(2, '0');
            const s = Math.floor((elapsed % 60000) / 1000).toString().padStart(2, '0');
            this.uptime.set(`${h}:${m}:${s}`);
        }, 1000);
    }

    ngOnDestroy() {
        if (this.eventSource) {
            this.eventSource.close();
        }
        if (this.logPollingInterval) {
            clearInterval(this.logPollingInterval);
        }
    }
}
