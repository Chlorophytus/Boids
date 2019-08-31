float4 calc_delta_angles(float4 a, float4 b) {
  // get A's delta
  float4 aa = (float4)(a.zw - a.xy, 0.0f, 0.0f);
  
  // get B's delta...
  float4 bb = (float4)(b.zw - b.xy, 0.0f, 0.0f);
  
  // get B - A. This determines how the angles deviate.
  float4 ba = fast_normalize(bb - aa);
  
  // get the arctangent of `ba` so we can get the delta angles
  ba.z = atan2(ba.y, ba.x);
  
  // aaaand return
  return ba.zzzz;
}

float4 move_forth(float4 a) {
  // hmmmm, what is our angle?
  // cartesian to polar:
  float4 aax = native_cos(a);
  float4 aay = native_sin(a);
  // norm then scale
  float4 xy = fast_normalize((float4)(aax.x, aay.y, 0.0f, 0.0f));
  return xy.xxyy / (float4)(128.0f);
}

float4 calc_delta_distance(float4 a) {
  return (float4)(native_rsqrt(fast_distance(a.xy, a.zw)));
}

kernel void boid_kernel(global float4 *bpos) {
  // okay, the bpos of each is
  // x = normal X pos 0-1
  // y = normal Y pos 0-1
  // z = normal delta of x 0-1 (please don't denorm me to zero)
  // w = normal delta of y 0-1
  int this = get_global_id(0);
  int pivot;
  float4 bangle;
  float4 binfluence;
  float4 pivot_influence;
  float4 back_off = (float4)(1.0f / 512.0f);
  
  for(int i = 0; i < NUM_BOIDS; i++) {
    if(this != i) {
      bangle = calc_delta_angles(bpos[this], bpos[i]);
      binfluence = calc_delta_distance((float4)(bpos[this].xy, bpos[i].xy));
      if((isless(binfluence.x, pivot_influence.x) != 0) && (isgreater(binfluence.x, back_off.x) != 0)) {
        pivot_influence = binfluence;
        pivot = i;
      }
    }
  }
  bpos[this] += move_forth(bangle);
}