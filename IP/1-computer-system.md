- [1. 25/04/23](#1-250423)
  - [1.1. Storage: Primary and secondary](#11-storage-primary-and-secondary)
  - [1.2. Booting](#12-booting)
  - [1.3. Charles Babbage](#13-charles-babbage)
  - [1.4. The most important input device is the keyboard.](#14-the-most-important-input-device-is-the-keyboard)
  - [1.5. The CPU](#15-the-cpu)
- [2. 26/04/23](#2-260423)
  - [2.1. Software](#21-software)
  - [2.2. Booting](#22-booting)
  - [2.3. RAM](#23-ram)
- [3. 27/04/23](#3-270423)
  - [3.1. Railway systems/services use DOS](#31-railway-systemsservices-use-dos)
  - [3.2. Machine Language](#32-machine-language)
  - [3.3. Binary to Decimal](#33-binary-to-decimal)
  - [3.4. High-Level Language](#34-high-level-language)


### 1. 25/04/23

#### 1.1. Storage: Primary and secondary

Primary: RAM and ROM

#### 1.2. Booting

Booting is the process of starting up a computer and loading the necessary software to make it operational. It includes hardware checks, loading the operating system, and initializing system components.

The OS is stored in the hard disk.

#### 1.3. Charles Babbage

Charles Babbage is known as the father of the computer because he designed and developed the first mechanical computer in the 19th century.

#### 1.4. The most important input device is the keyboard.

Input devices: Keyboard, mouse, joystick, scanner, light pen, microphone, etc.

Output devices: Monitor, speaker, printer, headphones, projector, etc.

#### 1.5. The CPU

The CPU is logically divided into three parts, i.e., ALU, CU, and MU.

Arithmetic Logic Unit: performs mathematical operations such as addition, multiplication, subtraction, and division. It also performs logical operations such as comparisons and Boolean operations.

Control Unit: controls the flow of data between the CPU and other components of the computer.

Memory Unit: stores data or instructions temporarily or permanently, including primary and secondary memory.

The CPU powers and operates/communicates with all peripheral devices.

Drivers are required to use any peripheral device.

- They usually come on compact disks or can be installed from the internet.
- These drivers are an introductory part between the computer and peripherals and require an installation process to be usable.

Plug and play devices: the devices that are designed to be recognized and configured automatically by a computer without the user manually configuring any settings or installing additional drivers. E.g., pen drive, mobile phones, etc.

---

### 2. 26/04/23

#### 2.1. Software

Software: System (operating system) and application (depends on requirements)

OS is the basic knowledge of the computer.

Windows was made by Microsoft first released in 1985.

Pirated software is allowed for individual use but not for businesses.

Some OS is free but they don't have all the functionalities.

Android is Linux but with modifications.

Windows is called windows because it depicts a window but can't touch the things inside it.

Application software is also installed in the secondary memory.

Upon pressing the power button, OS copies from secondary to the primary memory.

#### 2.2. Booting

Booting: warm and cold.

Cold booting: the computer was turned off at first.
Warm booting: shut down and start again (restart)

#### 2.3. RAM

- Its full form is Random Access Memory
- It is a primary memory.
- Has a particular size.
- It is temporary storage.
- Overloading leads to hangs and crashes.

Downloaded files are first stored in the RAM and then exported to the secondary memory.

Increasing the RAM is a permanent solution to use a lot of software together.

CD: Compact disk
DVD: Digital Versatile Disk

Some disks are rewritable but can only be done a few times, and rewriting it needs to fully wipe the memory.

---

### 3. 27/04/23

#### 3.1. Railway systems/services use DOS

DOS: Disk Operating System

There was no concept of a hard disk in the old days, so the OS is stored on a CD.

Till now, modern PCs can also run DOS, but the disk is not required as the OS can be stored on the hard disk.

Linux is the most popular among free OS.

Reasons to use Linux:

- Virus-free
- Modifiable
- Free to use
- Lightweight

#### 3.2. Machine Language

A computer can only understand signals, i.e., high voltage (1) and low voltage (0).

"High voltage" and "low voltage" are hard to read and write on a human scale because it's time-consuming, so these are written as binary.

All the alphabets, numbers, punctuation marks, and space are only recognized as a picture in a computer, and each one of them is recognized as a particular signal.

#### 3.3. Binary to Decimal

A = 1000001

1`*`2^6 + 0`*`2^5 + 0`*`2^4 + 0`*`2^3 + 0`*`2^2 + 1`*`2^0
=> 65

Therefore, B = 66

ASCII, abbreviated from American Standard Code for Information Interchange, is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices.

95 is the ASCII value for '\_'

Upon division of 97 with 2 and the other quotients and getting the remainder, we get the number 010011; this is called ASCII code.

#### 3.4. High-Level Language

Computer languages (C, C++, JS, Java, Python, etc.) are called high-level languages.

Compiler and interpreter translate high-level language into machine code.

```java
public class Acid {
    public static void main(String[] args) {
        int a, b = 5, c = 10;
        a = b + c;
        System.out.println(a);
    }
}
```
