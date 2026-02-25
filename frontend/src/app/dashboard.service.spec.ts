import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { DashboardService } from './dashboard.service';
import { environment } from '../environments/environment';

// Mock EventSource for Node/Vitest environment
if (typeof window !== 'undefined') {
    (window as any).EventSource = class {
        constructor(url: string) { }
        onmessage = null;
        onerror = null;
        close() { }
        addEventListener() { }
        removeEventListener() { }
    };
}

describe('DashboardService', () => {
    let service: DashboardService;
    let httpMock: HttpTestingController;

    beforeEach(() => {
        TestBed.configureTestingModule({
            imports: [HttpClientTestingModule],
            providers: [DashboardService]
        });
        service = TestBed.inject(DashboardService);
        httpMock = TestBed.inject(HttpTestingController);

        // Flush construction-time requests
        httpMock.expectOne(`${environment.apiUrl}/face/`).flush({ success: true, names: [] });
        httpMock.expectOne({ url: `${environment.apiUrl}/logs/?limit=50`, method: 'GET' }).flush({ success: true, logs: [] });
    });

    afterEach(() => {
        httpMock.verify();
        if (service) service.ngOnDestroy();
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });

    it('should fetch registered faces', () => {
        const mockNames = ['Alice', 'Bob'];
        service.fetchRegisteredFaces();

        const req = httpMock.expectOne(`${environment.apiUrl}/face/`);
        expect(req.request.method).toBe('GET');
        req.flush({ success: true, names: mockNames });

        expect(service.registeredNames()).toEqual(mockNames);
    });

    it('should add a log entry', () => {
        const logText = 'Test log message';
        service.addLog(logText, 'info');

        expect(service.logs().length).toBe(1);
        expect(service.logs()[0].text).toBe(logText);
    });

    it('should call register API', () => {
        const name = 'New User';
        service.registerFace(name).subscribe(res => {
            expect(res.success).toBe(true);
        });

        const req = httpMock.expectOne(`${environment.apiUrl}/face/register`);
        expect(req.request.method).toBe('POST');
        expect(req.request.body).toEqual({ name });
        req.flush({ success: true, message: 'Done' });
    });
});
