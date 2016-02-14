void setup() {
  print(isInsideRect(4,4,1,5,5,5,1,2,5,2));
}

void draw() {
}

boolean isInsideRect(int pointX, int pointY, int rectX, int rectY, int rectX2, int rectY2, int rectX3, int rectY3, int rectX4, int rectY4) {
  int largestX = rectX;
  int smallestX = rectX;

  int largestY = rectY;
  int smallestY = rectY;

  int[] rectXs = {rectX, rectX2, rectX3, rectX4};
  int[] rectYs = {rectY, rectY2, rectY3, rectY4};

  for (int i = 0; i < 4; i++) //finds largest in array
    if (rectXs[i] > largestX)
      largestX = rectXs[i];
    
  for (int i = 0; i < 4; i++) //find smallest in array
    if (rectXs[i] < smallestX) 
      smallestX = rectXs[i];

  for (int i = 0; i < 4; i++)
    if (rectYs[i] > largestY) 
      largestY = rectYs[i];
    
  for (int i = 0; i < 4; i++) 
    if (rectYs[i] < smallestY) 
      smallestY = rectYs[i];
    

  if (pointX > smallestX && pointX < largestX && pointY > smallestY && pointY < largestY) //if point inside box
    return true;
  
  return false;
}