import { TestBed, ComponentFixture } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { App } from './app';
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

describe('App', () => {
  let fixture: ComponentFixture<App>;
  let httpMock: HttpTestingController;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App, HttpClientTestingModule],
    }).compileComponents();

    fixture = TestBed.createComponent(App);
    httpMock = TestBed.inject(HttpTestingController);

    // Flush construction-time requests from DashboardService
    httpMock.expectOne(`${environment.apiUrl}/face/`).flush({ success: true, names: [] });
    httpMock.expectOne({ url: `${environment.apiUrl}/logs/?limit=50`, method: 'GET' }).flush({ success: true, logs: [] });
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should create the app', () => {
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should render title', async () => {
    await fixture.whenStable();
    fixture.detectChanges();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h1')?.textContent).toContain('BIOMETRIC_CONTROL_CENTER');
  });
});
