# 2x2-Rubik-s-Cube-Solver---Adi-R
Find a white corner on any part of your cube and put it at the top left corner of your front face
Input the faces as follows: suppose the Front is W|B, you would input it into Front as W B Y R, no quotations, no commas, only spaces separating the colors.
                                                 Y|R
For inputing the faces W=White, B=Blue, R=Red, O=Orange, G=Green, Y=Yellow
You would follow the same pattern for the other faces too, for example, entering Above would be done by tilting the cube downwards so that Above becomes the Front and then following the same format for Front
P.S. for entering the Back side, the only way to do it is to first flip the cube vertically so Above becomes Front and then flip it vertically again. In other words, just take your Front side and run the algorithm L', R', L', R' and then enter Back. DO NOT MAKE THE RIGHT SIDE FRONT AND THEN FLIP IT HORIZONTALLY AGAIN SO BACK WILL BECOME FRONT(A', U', A', U') THIS WILL MAJORLY SCREW UP THE CODE. 
If you're confused about what move notation means, suppose we have a perfectly solved cube, this would be our net     G|G,     Turning it right would give us G|W if you see
                                                                                                                      G|G                                     G|W           
                                                                                                                  R|R|W|W|O|O                             R|R|W|B|O|O
                                                                                                                  R|R|W|W|O|O                             R|R|W|B|O|O
                                                                                                                      B|B                                     B|Y
                                                                                                                      B|B                                     B|Y
                                                                                                                      Y|Y                                     Y|G
                                                                                                                      Y|Y                                     Y|G
An apostrophe after a turn, such as R' it means to turn it the other way; an algorithm like R, R' would just revert the cube back to its original state.
Good Luck!
