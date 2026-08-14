// Map your full training class names to shorter, user-friendly names

export const classNameMapping = {
  "Acne and Rosacea Photos": "Acne and Rosacea",
  "Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions": "Skin Cancer",
  "Atopic Dermatitis Photos": "Atopic Dermatitis",
  "Bullous Disease Photos": "Blistering Disease",
  "Eczema Photos": "Eczema",
  "Exanthems and Drug Eruptions": "Skin Rash",
  "Herpes HPV and other STDs Photos": "Viral Skin Infection", 
  "Light Diseases and Disorders of Pigmentation": "Pigmentation Disorder",
  "Lupus and other Connective Tissue diseases": "Lupus diseases",
  "Melanoma Skin Cancer Nevi and Moles": "Melanoma Skin Cancer",
  "Nail Fungus and other Nail Disease": "Nail Disease",
  "Psoriasis pictures Lichen Planus and related diseases": "Psoriasis",
  "Scabies Lyme Disease and other Infestations and Bites": "Scabies & Bites",
  "Seborrheic Keratoses and other Benign Tumors": "Benign Skin Growth",
  "Systemic Disease": "Systemic Disease",
  "Tinea Ringworm Candidiasis and other Fungal Infections": "Fungal Infection",
  "Vascular Tumors": "Vascular Tumor",
  "Vasculitis Photos": "Vasculitis",
  "Warts Molluscum and other Viral Infections": "Warts Molluscum"
};

export const formatClassName = (fullClassName) => {
  return classNameMapping[fullClassName] || fullClassName;
};