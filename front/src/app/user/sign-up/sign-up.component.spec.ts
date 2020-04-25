import { async, ComponentFixture, TestBed, inject } from '@angular/core/testing';
import { SignUpComponent } from './sign-up.component';
import { RouterTestingModule } from '../../../../node_modules/@angular/router/testing';
import { appRoutes } from '../../routes';
import { UserService } from '../../shared/user.service';
import { UserComponent } from '../user.component';
const router = '../../routes.ts';

describe('SignUpComponent', () => {
  let component: SignUpComponent;
  // let hostcomponent: UserComponent;
  let hostfixture: ComponentFixture<UserComponent>;
  let fixture: ComponentFixture<SignUpComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [RouterTestingModule.withRoutes(appRoutes)],
      declarations: [ SignUpComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    hostfixture = TestBed.createComponent(UserComponent);
    fixture = TestBed.createComponent(SignUpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeDefined();
  });
});
