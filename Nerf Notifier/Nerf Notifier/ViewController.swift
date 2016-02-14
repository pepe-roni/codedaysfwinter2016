//
//  ViewController.swift
//  Nerf Notifier
//
//  Created by Jesse Liang on 2/13/16.
//  Copyright © 2016 Jesse Liang. All rights reserved.
//

import UIKit
import AudioToolbox

class ViewController: UIViewController {
    
    var headStatus = "false"
    var leftArmStatus = "false"
    var rightArmStatus = "false"
    var torsoStatus = "false"
    var leftLegStatus = "false"
    var rightLegStatus = "false"
    
    var head2Status = "false"
    var leftArm2Status = "false"
    var rightArm2Status = "false"
    var torso2Status = "false"
    var leftLeg2Status = "false"
    var rightLeg2Status = "false"
    
    var head = String()
    var leftArm = String()
    var rightArm = String()
    var leftLeg = String()
    var rightLeg = String()
    var torso = String()
    
    var head2 = String()
    var leftArm2 = String()
    var rightArm2 = String()
    var leftLeg2 = String()
    var rightLeg2 = String()
    var torso2 = String()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        head = "head0.png"
        torso = "torso0"
        leftArm = "leftA0L0"
        rightArm = "rightA0L0"
        leftLeg = "leftL0A0"
        rightLeg = "rightL0A0"
        
        head2 = "head0.png"
        torso2 = "torso0"
        leftArm2 = "leftA0L0"
        rightArm2 = "rightA0L0"
        leftLeg2 = "leftL0A0"
        rightLeg2 = "rightL0A0"
        
        headFunc()
        torsoFunc()
        rightArmFunc()
        leftLegFunc()
        rightLegFunc()
        leftArmFunc()
        
        head2Func()
        torso2Func()
        rightArm2Func()
        leftLeg2Func()
        rightLeg2Func()
        leftArm2Func()
        
    }
    
    func headFunc() {
        
        let headImage = UIImage(named: head)
        let headImageView = UIImageView(image: headImage!)
        headImageView.frame = CGRect(x: 182, y: 20, width: 181.25, height: 66.75)
        view.addSubview(headImageView)
        
    }
    
    func torsoFunc() {
        
        let torsoImage = UIImage(named: torso)
        let torsoImageView = UIImageView(image: torsoImage!)
        torsoImageView.frame = CGRect(x: 266.75, y: 86.75, width: 72.75, height: 183)
        view.addSubview(torsoImageView)
        
    }
    
    func leftArmFunc() {
        
        let leftArmImage = UIImage(named: leftArm)
        let leftArmImageView = UIImageView(image: leftArmImage!)
        leftArmImageView.frame = CGRect(x: 339.5, y: 86.75, width: 74.5, height: 183)
        view.addSubview(leftArmImageView)

    }
    
    func rightArmFunc() {
        
        let rightArmImage = UIImage(named: rightArm)
        let rightArmImageView = UIImageView(image: rightArmImage!)
        rightArmImageView.frame = CGRect(x: 182, y: 86.75, width: 84.75, height: 183)
        view.addSubview(rightArmImageView)
        
    }
    
    func leftLegFunc() {
        
        let leftLegImage = UIImage(named: leftLeg)
        let leftLegImageView = UIImageView(image: leftLegImage!)
        leftLegImageView.frame = CGRect(x: 303.5, y: 269.75, width: 110.5, height: 214.25)
        view.addSubview(leftLegImageView)
        
    }
    
    func rightLegFunc() {
        
        let rightLegImage = UIImage(named: rightLeg)
        let rightLegImageView = UIImageView(image: rightLegImage!)
        rightLegImageView.frame = CGRect(x: 182, y: 269.75, width: 121.5, height: 214.25)
        view.addSubview(rightLegImageView)
        
    }
    
    func head2Func() {
        
        let head2Image = UIImage(named: head2)
        let head2ImageView = UIImageView(image: head2Image!)
        head2ImageView.frame = CGRect(x: 0, y: 272, width: 181.25, height: 66.75)
        view.addSubview(head2ImageView)
        
    }
    
    func leftArm2Func() {
        
        let leftArm2Image = UIImage(named: leftArm2)
        let leftArm2ImageView = UIImageView(image: leftArm2Image!)
        leftArm2ImageView.frame = CGRect(x: 157.5, y: 338.75, width: 74.5, height: 183)
        view.addSubview(leftArm2ImageView)
        
    }
    
    func torso2Func() {
        
        let torso2Image = UIImage(named: torso2)
        let torso2ImageView = UIImageView(image: torso2Image!)
        torso2ImageView.frame = CGRect(x: 84.75, y: 338.75, width: 72.75, height: 183)
        view.addSubview(torso2ImageView)
    
    }
    
    func rightArm2Func() {
        
        let rightArm2Image = UIImage(named: rightArm2)
        let rightArm2ImageView = UIImageView(image: rightArm2Image!)
        rightArm2ImageView.frame = CGRect(x: 0, y: 338.75, width: 84.75, height: 183)
        view.addSubview(rightArm2ImageView)
    
    }
    
    func leftLeg2Func() {
    
        let leftLeg2Image = UIImage(named: leftLeg2)
        let leftLeg2ImageView = UIImageView(image: leftLeg2Image!)
        leftLeg2ImageView.frame = CGRect(x: 121.5, y: 521.75, width: 110.5, height: 214.25)
        view.addSubview(leftLeg2ImageView)
        
    }
    
    func rightLeg2Func() {
    
        let rightLeg2Image = UIImage(named: rightLeg2)
        let rightLeg2ImageView = UIImageView(image: rightLeg2Image!)
        rightLeg2ImageView.frame = CGRect(x: 0, y: 521.75, width: 121.5, height: 214.25)
        view.addSubview(rightLeg2ImageView)
    
    }
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(true)
        
        leftArmHit()
        
        _ = NSTimer.scheduledTimerWithTimeInterval(0.1, target: self, selector: Selector("update"), userInfo: nil, repeats: true)
    }
    
    func update () {
        
        dispatch_async(dispatch_get_main_queue(), {
            
            AudioServicesPlayAlertSound(SystemSoundID(kSystemSoundID_Vibrate))
        })
    }
    
    func headHit() {
        
        head = "head1"
        
        headFunc()
    }
    
    func leftArmHit() {
        
        if leftLegStatus == "false" {
            leftLeg = "leftL0A1"
            leftArm = "leftA1L0"
        } else {
            leftLeg = "leftL1A1"
            leftArm = "leftA1L1"
        }
        
        leftArmFunc()
        leftLegFunc()
    }
    
    func rightArmHit() {
        
        if rightLegStatus == "false" {
            rightLeg = "rightL0A1"
            rightArm = "rightA1L0"
        } else {
            rightLeg = "rightL1A1"
            rightArm = "rightA1L1"
        }
        
        rightArmFunc()
        rightLegFunc()
    }
    
    func torsoHit() {
        
        torso = "torso1"
        
        torsoFunc()
    }
    
    func leftLegHit() {

        if leftArmStatus == "false" {
            leftArm = "leftA1L0"
            leftLeg = "leftL0A1"
        } else {
            leftArm = "leftA1L1"
            leftLeg = "leftL1A1"
        }
        
        leftArmFunc()
        leftLegFunc()
    }
    
    func rightLegHit() {
        
        if rightArmStatus == "false" {
            rightArm = "rightA0L1"
            rightLeg = "rightL1A0"
        } else {
            rightArm = "rightA1L1"
            rightLeg = "rightL1A1"
        }
        
        rightArmFunc()
        rightLegFunc()
    }
    
    func head2Hit() {
        
        head2 = "head1"
        
        head2Func()
    }
    
    func leftArm2Hit() {
        
        if leftLeg2Status == "false" {
            leftLeg2 = "leftL0A1"
            leftArm2 = "leftA1L0"
        } else {
            leftLeg2 = "leftL1A1"
            leftArm2 = "leftA1L1"
        }
        
        leftArm2Func()
        leftLeg2Func()
    }
    
    func rightArm2Hit() {
        
        if rightLeg2Status == "false" {
            rightLeg2 = "rightL0A1"
            rightArm2 = "rightA1L0"
        } else {
            rightLeg2 = "rightL1A1"
            rightArm2 = "rightA1L1"
        }
        
        rightArm2Func()
        rightLeg2Func()
    }
    
    func torso2Hit() {
        
        torso2 = "torso1"
        
        torso2Func()
    }
    
    func leftLeg2Hit() {
        
        if leftArm2Status == "false" {
            leftArm2 = "leftA1L0"
            leftLeg2 = "leftL0A1"
        } else {
            leftArm2 = "leftA1L1"
            leftLeg2 = "leftL1A1"
        }
        
        leftArm2Func()
        leftLeg2Func()
    }
    
    func rightLeg2Hit() {
        
        if rightArm2Status == "false" {
            rightArm2 = "rightA0L1"
            rightLeg2 = "rightL1A0"
        } else {
            rightArm2 = "rightA1L1"
            rightLeg2 = "rightL1A1"
        }
        
        rightArm2Func()
        rightLeg2Func()
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

