# **Oculai_P_Challenge**
This project is part of Oculai Internship challenge

**Task:** Create a script which tracks the progress of various Construction work from the provided video

**Solution:** Task for *Formwork and Concreting* was attempted and the solution is as follows:

**Libraries used:** OpenCV and NumPy

**Method:** For **Formwork tasks**, the method of counting the color of the pixels in the area of interest was used to monitor the progress of the work.
            Individual frames were first cropped and then the pixels of interest in that area were counted and output was written over the frames and solution video             file was then stitched.
            For **Concreting Video tasks**, the 4th and 5th frames had strong shadow of the crane in the image, I tried to use various filtering techniques like *Canny Edge Detection, SimpleBlobDetector, Laplacian Filter, Find Contours & Pyramid Mean Shift Filter*. Results from **Pyramid Mean Shift Filter** were the best               and reliable. Hence, it was used in the final code. Techniques to remove shadows and segmentation was used but the performance was very much hampered due to many noises (construction workers, shadow, and equipment).
             
**Sample cropped image:**

![cropped](https://user-images.githubusercontent.com/25361247/127643946-23847ae9-4f08-4238-a893-2ec32e02a7e8.jpg)

**Sample output image:** ![2](https://user-images.githubusercontent.com/25361247/127644104-bfce6aa4-a3f7-4186-b918-9e132ba4e836.jpg)

**Results:** The progress of Concreting and Formwork can be tracked to a fair accuracy by using the method of counting pixels.
