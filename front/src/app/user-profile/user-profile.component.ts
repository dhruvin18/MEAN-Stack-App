import { Component, OnInit } from '@angular/core';
import { UserService } from '../shared/user.service';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';
import { formatDate } from '../../../node_modules/@angular/common';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
  userDetails;
  query = false;
  serverErrorMessages: string;
  functionDebug: string;
  functionDebug1: string;
  case;
  svmclass;
  nbclass;
  rfclass;
  lrclass;
  knnclass;
  d2vsvmclass;
  d2vrfclass;
  d2vlrclass;
  d2vknnclass;
  bowsvmclass;
  bownbclass;
  bowrfclass;
  bowlrclass;
  bowknnclass;
  classerror;
  files;
  lr = 'Logistic Regression';
  nb = 'Naive Bayes';
  rf = 'Random Forest';
  svm = 'SVM';
  knn = 'k Nearest Neighbour';
  d2vsvm = 'D2VSVM';
  d2vrf = 'D2VLR';
  d2vlr = 'D2VRf';
  d2vknn = 'D2VKNN';
  bowsvm = 'BOWSVM';
  bowrf = 'BOWRF';
  bowlr = 'BOWLR';
  bownb = 'BOWNB';
  bowknn = 'BOWKNN';
  // keywords: string[];
  keywords;
  confidence: number[];
  extraction;
  constructor(private userService: UserService, private router: Router) { }

  model = {
    data: '',
  };

  ngOnInit(): void {
    this.userService.getUserProfile().subscribe(
      res => {
        const temp = 'user';
        this.userDetails = res[temp];
      },
      err => {}
    );
  }


  onSubmit(form: NgForm) {
    this.query = true;
    const formdata = form.value;
    // this.userService.extractKeywords(form.value).subscribe(
    //   res => {
    //     // this.functionDebug = JSON.stringify(res[0]);
    //     const text = 'text';
    //     const temp = 'extractions';
    //     const temp1 = 'parsed_value';
    //     this.keywords = res[0][temp];
    //     // this.case = res[0][text];
    //   },
    //   err => {
    //     this.functionDebug = err.errors;
    //   }
    // );
    // this.userService.get_files(form.value).subscribe(
    //   res => {
    //     const filenames = 'filenames';
    //     this.files = res[filenames];
    //   }
    // );
    this.userService.predict_label(form.value).subscribe(
      res => {
        const data = 'case';
        this.case = res[data];
        this.lrclass = res[this.lr];
        this.nbclass = res[this.nb];
        this.rfclass = res[this.rf];
        this.knnclass = res[this.knn];
        this.svmclass = res[this.svm];
        this.d2vsvmclass = res[this.d2vsvm];
        this.d2vrfclass = res[this.d2vrf];
        this.d2vlrclass = res[this.d2vlr];
        this.d2vknnclass = res[this.d2vknn];
        this.bowsvmclass = res[this.bowsvm];
        this.bowknnclass = res[this.bowknn];
        this.bowrfclass = res[this.bowrf];
        this.bowlrclass = res[this.bowlr];
        this.bownbclass = res[this.bownb];
        this.query = false;
        const filenames = 'filenames';
        this.files = res[filenames];
      },
      err => {
        this.classerror = err.errors;
      }
    );
  }

  onLogout() {
    this.userService.deleteToken();
    this.router.navigateByUrl('/login');
  }
}
