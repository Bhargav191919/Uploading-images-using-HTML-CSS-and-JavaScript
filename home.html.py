#!/usr/bin/env python
# coding: utf-8

# In[ ]:


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href='https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="style.css">
    <title>Upload Images</title>
</head>
<body>
    
    <div class="container">
        <input type="file" id="file" accept="image/*" hidden>
        <div class="img-area" data-img="">
            <i class='bx bxs-cloud-upload icon'></i>
            <h3>Upload Image</h3>
            <p>Image size must be less than <span>2MB</span></p>
        </div>
        <button class="select-image">Select Image</button>
    </div>

    <script src="script.js"></script>
</body>
</html>

